import time
import random
import threading
import os

# Initialize the global variables
crypto = 0
money = 0
miners = 0
miner_level = 1
miner_upgrade_cost = 500
dev_mode = False  # Global variable to track developer mode

# Define costs for new items
gpu_rig_cost = 2000
asic_miner_cost = 5000
energy_booster_cost = 1000

def estimate_sell():
    # Simulate a random fee between 5% and 15%
    fee_percentage = random.uniform(5, 15) / 100
    sell_amount = crypto * (1 - fee_percentage)
    return sell_amount, fee_percentage

def miner_efficiency(level):
    # Define efficiency for each level
    efficiency = {1: (1, 10), 2: (2, 20), 3: (3, 30), 4: (4, 40), 5: (5, 50)}
    return efficiency.get(level, (5, 50))  # Default to level 5 efficiency if level is higher

def auto_mine():
    global crypto
    while True:
        if miners > 0:
            min_mine, max_mine = miner_efficiency(miner_level)
            mined_amount = miners * random.randint(min_mine, max_mine)  # Each miner mines crypto based on its level
            crypto += mined_amount
            print(f"\nAuto-mined {mined_amount} crypto. Total crypto: {crypto}")
        time.sleep(60)  # Auto-mine every 60 seconds

def clear_console():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def dev_mode_commands():
    print("Developer Mode Commands:")
    print("1. show_all - Show detailed information about the game state.")
    print("2. reset - Reset all game variables to their initial values.")
    print("3. add_money <amount> - Add specified amount of money.")
    print("4. add_crypto <amount> - Add specified amount of crypto.")
    print("5. set_miners <number> - Set the number of miners.")
    print("6. set_miner_level <level> - Set the miner level.")
    print("7. upgrade_miner - Upgrade the miner level and cost.")
    print("8. exit_dev - Exit developer mode.")

def main():
    global crypto  # Declare that we are using the global variable 'crypto'
    global money
    global miners
    global miner_level
    global miner_upgrade_cost
    global dev_mode

    # Start the auto-mining thread
    auto_mine_thread = threading.Thread(target=auto_mine, daemon=True)
    auto_mine_thread.start()
    
    while True:
        # Display the command prompt
        if dev_mode:
            command = input("DEV_CMD> ").strip().lower()
        else:
            command = input("CMD> ").strip().lower()
        
        if command == "dev_mode=on":
            dev_mode = True
            print("Developer mode activated.")
            dev_mode_commands()
        elif command == "dev_mode=off":
            dev_mode = False
            print("Developer mode deactivated.")
        elif command == "hack":
            confirmation = input("Are you sure? (yes/no): ").strip().lower()
            if confirmation == "yes":
                print("Initiating hack...")
                time.sleep(1)  # 1 second delay
                print("Hacking in progress...")
                time.sleep(1)
                for i in range(1, 101):
                    print(f"Hack {i}%...")
                    time.sleep(0.1)
                print("Hack completed...")
                crypto += random.randint(1, 10000)  # Update the global variable with a random number between 1 and 10,000
                print(f"Crypto: {crypto} and ${money}")
            elif confirmation == "no":
                print("Hack canceled")
            else:
                print("Invalid response. Hack canceled.")
        elif command == "mine":
            mine_time = random.randint(1, 75)
            print("Mining crypto...")
            for remaining in range(mine_time, 0, -1):
                print(f"Time left: {remaining} seconds...", end='\r')
                time.sleep(1)
            mined_amount = random.randint(1, 1000)  # Random amount of crypto mined between 1 and 1000
            crypto += mined_amount
            print("Mine completed...")
            print(f"\nMined {mined_amount} crypto. Total crypto: {crypto} and ${money}")
        elif command == "exit":
            print("Exiting the program.")
            break
        elif command == "sell":
            if crypto > 0:
                sell_amount, fee_percentage = estimate_sell()
                fee = crypto * fee_percentage
                crypto -= (sell_amount + fee)  # Remove the entire amount of crypto
                money += sell_amount  # Convert 90% of the crypto to money
                print(f"Sold {sell_amount:.2f} crypto at a fee of {fee_percentage*100:.2f}%. Total crypto: {crypto:.2f} and ${money:.2f}")
            else:
                print("No crypto to sell.")
        elif command == "estimate":
            if crypto > 0:
                sell_amount, fee_percentage = estimate_sell()
                print(f"If you sell now, you will get {sell_amount:.2f} crypto after a fee of {fee_percentage*100:.2f}%.")
            else:
                print("No crypto to estimate.")
        elif command == "buy":
            print("Available items to buy:")
            print("1. Crypto Miner - $1000 (mines crypto automatically every minute)")
            print(f"2. Upgrade Miner - ${miner_upgrade_cost} (current level: {miner_level}, increases mining efficiency)")
            print(f"3. GPU Rig - ${gpu_rig_cost} (increases mining efficiency by 50%)")
            print(f"4. ASIC Miner - ${asic_miner_cost} (mines crypto 2x faster than regular miners)")
            print(f"5. Energy Booster - ${energy_booster_cost} (reduces mining cost by 10%)")
            item = input("Enter the item number you want to buy: ").strip()
            if item == "1":
                if money >= 1000:
                    miners += 1
                    money -= 1000
                    print(f"Bought a Crypto Miner. Total miners: {miners}. Remaining money: ${money:.2f}")
                else:
                    print("Not enough money to buy a Crypto Miner.")
            elif item == "2":
                if money >= miner_upgrade_cost:
                    miner_level += 1
                    money -= miner_upgrade_cost
                    miner_upgrade_cost = int(miner_upgrade_cost * 1.5)  # Increase the cost for the next upgrade
                    min_mine, max_mine = miner_efficiency(miner_level)
                    print(f"Upgraded miners to level {miner_level}. Now mines between {min_mine} and {max_mine} crypto per minute per miner.")
                    print(f"Remaining money: ${money:.2f}. Next upgrade cost: ${miner_upgrade_cost}")
                else:
                    print("Not enough money to upgrade miners.")
            elif item == "3":
                if money >= gpu_rig_cost:
                    miner_level += 1  # Boost mining efficiency
                    money -= gpu_rig_cost
                    print(f"Bought a GPU Rig. Miner level increased. Remaining money: ${money:.2f}")
                else:
                    print("Not enough money to buy a GPU Rig.")
            elif item == "4":
                if money >= asic_miner_cost:
                    miners += 2  # ASIC miners are more efficient
                    money -= asic_miner_cost
                    print(f"Bought an ASIC Miner. Total miners: {miners}. Remaining money: ${money:.2f}")
                else:
                    print("Not enough money to buy an ASIC Miner.")
            elif item == "5":
                if money >= energy_booster_cost:
                    # Reduce mining costs or increase efficiency
                    money -= energy_booster_cost
                    print(f"Bought an Energy Booster. Mining costs reduced. Remaining money: ${money:.2f}")
                else:
                    print("Not enough money to buy an Energy Booster.")
            else:
                print("Invalid item number.")
        elif command == "help":
            print("Show command to show current crypto, money balances, and miner info...")
            print("Mine command to mine crypto...")
            print("Exit command to close...")
            print("Hack command to hack crypto...")
            print("Sell command to sell crypto and convert it to money (random fee between 5% and 15%)...")
            print("Estimate command to estimate how much you will get if you sell now...")
            print("Buy command to purchase items like crypto miners, GPU rigs, ASIC miners, or energy boosters...")
            print("Clear command to clear the console...")
        elif command == "show":
            min_mine, max_mine = miner_efficiency(miner_level)
            print(f"Crypto: {crypto:.2f}, Money: ${money:.2f}, Miners: {miners}, Miner Level: {miner_level}, Upgrade Cost: ${miner_upgrade_cost}")
            print(f"Each miner mines between {min_mine} and {max_mine} crypto per minute at current level.")
        elif command == "clear":
            clear_console()
        elif dev_mode:
            # Developer mode specific commands
            if command == "show_all":
                print(f"Developer Mode Information:\nCrypto: {crypto:.2f}, Money: ${money:.2f}, Miners: {miners}, Miner Level: {miner_level}, Upgrade Cost: ${miner_upgrade_cost}")
                print("Available commands for the developer mode:")
                dev_mode_commands()
            elif command.startswith("add_money "):
                try:
                    amount = float(command.split()[1])
                    money += amount
                    print(f"Added ${amount:.2f} to your money. New balance: ${money:.2f}")
                except ValueError:
                    print("Invalid amount.")
            elif command.startswith("add_crypto "):
                try:
                    amount = float(command.split()[1])
                    crypto += amount
                    print(f"Added {amount:.2f} crypto. New balance: {crypto:.2f}")
                except ValueError:
                    print("Invalid amount.")
            elif command.startswith("set_miners "):
                try:
                    amount = int(command.split()[1])
                    miners = amount
                    print(f"Set number of miners to {miners}.")
                except ValueError:
                    print("Invalid number.")
            elif command.startswith("set_miner_level "):
                try:
                    level = int(command.split()[1])
                    miner_level = level
                    min_mine, max_mine = miner_efficiency(miner_level)
                    print(f"Set miner level to {miner_level}. Now mines between {min_mine} and {max_mine} crypto per minute per miner.")
                except ValueError:
                    print("Invalid level.")
            elif command == "upgrade_miner":
                miner_level += 1
                money -= miner_upgrade_cost
                miner_upgrade_cost = int(miner_upgrade_cost * 1.5)  # Increase the cost for the next upgrade
                min_mine, max_mine = miner_efficiency(miner_level)
                print(f"Upgraded miners to level {miner_level}. Now mines between {min_mine} and {max_mine} crypto per minute per miner.")
                print(f"Remaining money: ${money:.2f}. Next upgrade cost: ${miner_upgrade_cost}")
            elif command == "exit_dev":
                dev_mode = False
                print("Exiting developer mode.")
            else:
                print("Unknown developer mode command.")
        else:
            print("Unknown command")

# Run the main function
if __name__ == "__main__":
    main()
