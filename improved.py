import random
import threading
import os
import time

class CryptoGame:
    def __init__(self):
        self.crypto = 0
        self.money = 0
        self.miners = 0
        self.miner_level = 1
        self.miner_upgrade_cost = 500
        self.hack_cooldown = 300  # 5 minutes cooldown between hacks
        self.last_hack_time = 0
        self.dev_mode = False
        self.gpu_rig_cost = 2000
        self.asic_miner_cost = 5000
        self.energy_booster_cost = 1000
        self.running = True

    def estimate_sell(self):
        fee_percentage = random.uniform(5, 15) / 100
        sell_amount = self.crypto * (1 - fee_percentage)
        return sell_amount, fee_percentage

    def miner_efficiency(self, level):
        efficiency = {1: (1, 10), 2: (2, 20), 3: (3, 30), 4: (4, 40), 5: (5, 50)}
        return efficiency.get(level, (5, 50))

    def auto_mine(self):
        while self.running:
            if self.miners > 0:
                min_mine, max_mine = self.miner_efficiency(self.miner_level)
                mined_amount = self.miners * random.randint(min_mine, max_mine)
                self.crypto += mined_amount
                print(f"\nAuto-mined {mined_amount} crypto. Total crypto: {self.crypto:.2f}")
            time.sleep(60)

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def process_command(self, command):
        if command == "dev_mode=on":
            self.activate_dev_mode()
        elif command == "dev_mode=off":
            self.dev_mode = False
            print("Developer mode deactivated.")
        elif command == "hack":
            self.hack()
        elif command == "mine":
            self.mine()
        elif command == "exit":
            self.exit_game()
        elif command == "sell":
            self.sell_crypto()
        elif command == "estimate":
            self.estimate_crypto()
        elif command == "buy":
            self.buy_items()
        elif command == "show":
            self.show_status()
        elif command == "clear":
            self.clear_console()
        elif command == "help":
            self.show_help()
        elif self.dev_mode:
            self.process_dev_mode_command(command)
        else:
            print("Unknown command")

    def activate_dev_mode(self):
        password = input("Enter developer mode password: ").strip()
        if password == "04-09-2013":
            self.dev_mode = True
            print("Developer mode activated.")
            self.dev_mode_commands()
        else:
            print("Incorrect password. Developer mode access denied.")

    def dev_mode_commands(self):
        print("Developer Mode Commands:")
        print("1. show_all - Show detailed information about the game state.")
        print("2. reset - Reset all game variables to their initial values.")
        print("3. add_money <amount> - Add specified amount of money.")
        print("4. add_crypto <amount> - Add specified amount of crypto.")
        print("5. set_miners <number> - Set the number of miners.")
        print("6. set_miner_level <level> - Set the miner level.")
        print("7. upgrade_miner - Upgrade the miner level and cost.")
        print("8. exit_dev - Exit developer mode.")

    def process_dev_mode_command(self, command):
        if command == "show_all":
            self.show_all()
        elif command.startswith("add_money "):
            self.add_money(command)
        elif command.startswith("add_crypto "):
            self.add_crypto(command)
        elif command.startswith("set_miners "):
            self.set_miners(command)
        elif command.startswith("set_miner_level "):
            self.set_miner_level(command)
        elif command == "upgrade_miner":
            self.upgrade_miner()
        elif command == "exit_dev":
            self.dev_mode = False
            print("Exiting developer mode.")
        else:
            print("Unknown developer mode command.")

    def hack(self):
        current_time = time.time()
        if current_time - self.last_hack_time < self.hack_cooldown:
            time_remaining = self.hack_cooldown - (current_time - self.last_hack_time)
            while time_remaining > 0:
                time_remaining = self.hack_cooldown - (current_time - self.last_hack_time)
                if time_remaining < 0:
                    time_remaining = 0
                print(f"\rUnable to hack. Please wait {int(time_remaining)} seconds...", end='')
                time.sleep(1)
                current_time = time.time()  # Update current time for accurate countdown
            
            # Clear the countdown message
            print("\rYou can now hack again.                         ", end='')
        
        # Proceed with the hack
        self.last_hack_time = time.time()
        success_chance = random.uniform(0, 1)
        
        if success_chance < 0.3:  # 30% chance of successful hack
            print("Hack in progress...")
            time.sleep(2)
            hacked_amount = random.randint(100, 10000)
            self.crypto += hacked_amount
            print(f"Hack successful! Gained {hacked_amount} crypto. Total crypto: {self.crypto:.2f}")
        else:  # 70% chance of failure
            print("Hack failed! You've been caught and fined.")
            fine_amount = random.randint(100, 500)
            self.money = max(0, self.money - fine_amount)
            print(f"You were fined ${fine_amount}. Remaining money: ${self.money:.2f}")

    def mine(self):
        mine_time = random.randint(1, 75)
        print("Mining crypto...")
        for remaining in range(mine_time, 0, -1):
            print(f"Time left: {remaining} seconds...", end='\r')
            time.sleep(1)
        mined_amount = random.randint(1, 1000)
        self.crypto += mined_amount
        print("\nMine completed...")
        print(f"Mined {mined_amount} crypto. Total crypto: {self.crypto:.2f} and ${self.money:.2f}")

    def exit_game(self):
        print("Exiting the program.")
        self.running = False

    def sell_crypto(self):
        if self.crypto > 0:
            sell_amount, fee_percentage = self.estimate_sell()
            fee = self.crypto * fee_percentage
            self.crypto -= (sell_amount + fee)
            self.money += sell_amount
            print(f"Sold {sell_amount:.2f} crypto at a fee of {fee_percentage*100:.2f}%. Total crypto: {self.crypto:.2f} and ${self.money:.2f}")
        else:
            print("No crypto to sell.")

    def estimate_crypto(self):
        if self.crypto > 0:
            sell_amount, fee_percentage = self.estimate_sell()
            print(f"If you sell now, you will get {sell_amount:.2f} crypto after a fee of {fee_percentage*100:.2f}%.")
        else:
            print("No crypto to estimate.")

    def buy_items(self):
        print("Available items to buy:")
        print("1. Crypto Miner - $1000 (mines crypto automatically every minute)")
        print(f"2. Upgrade Miner - ${self.miner_upgrade_cost} (current level: {self.miner_level}, increases mining efficiency)")
        print(f"3. GPU Rig - ${self.gpu_rig_cost} (increases mining efficiency by 50%)")
        print(f"4. ASIC Miner - ${self.asic_miner_cost} (mines crypto 2x faster than regular miners)")
        print(f"5. Energy Booster - ${self.energy_booster_cost} (reduces mining cost by 10%)")
        item = input("Enter the item number you want to buy: ").strip()

        if item == "1" and self.money >= 1000:
            self.miners += 1
            self.money -= 1000
            print(f"Bought a Crypto Miner. Total miners: {self.miners}. Remaining money: ${self.money:.2f}")
        elif item == "2" and self.money >= self.miner_upgrade_cost:
            self.miner_level += 1
            self.money -= self.miner_upgrade_cost
            self.miner_upgrade_cost = int(self.miner_upgrade_cost * 1.5)
            min_mine, max_mine = self.miner_efficiency(self.miner_level)
            print(f"Upgraded miners to level {self.miner_level}. Now mines between {min_mine} and {max_mine} crypto per minute per miner.")
            print(f"Remaining money: ${self.money:.2f}. Next upgrade cost: ${self.miner_upgrade_cost}")
        elif item == "3" and self.money >= self.gpu_rig_cost:
            self.miner_level += 1
            self.money -= self.gpu_rig_cost
            print(f"Bought a GPU Rig. Miner level increased. Remaining money: ${self.money:.2f}")
        elif item == "4" and self.money >= self.asic_miner_cost:
            self.miners += 2
            self.money -= self.asic_miner_cost
            print(f"Bought an ASIC Miner. Total miners: {self.miners}. Remaining money: ${self.money:.2f}")
        elif item == "5" and self.money >= self.energy_booster_cost:
            self.money -= self.energy_booster_cost
            print(f"Bought an Energy Booster. Mining costs reduced. Remaining money: ${self.money:.2f}")
        else:
            print("Invalid item number or not enough money.")

    def show_status(self):
        min_mine, max_mine = self.miner_efficiency(self.miner_level)
        print(f"Crypto: {self.crypto:.2f}, Money: ${self.money:.2f}, Miners: {self.miners}, Miner Level: {self.miner_level}, Upgrade Cost: ${self.miner_upgrade_cost}")
        print(f"Each miner mines between {min_mine} and {max_mine} crypto per minute at current level.")

    def show_help(self):
        print("Available commands:")
        print("show - Show current crypto, money balances, and miner info...")
        print("mine - Mine crypto...")
        print("exit - Close the program...")
        print("hack - Attempt to hack for crypto (risky)...")
        print("sell - Sell crypto and convert it to money (random fee between 5% and 15%)...")
        print("estimate - Estimate how much you will get if you sell now...")
        print("buy - Purchase items like crypto miners, GPU rigs, ASIC miners, or energy boosters...")
        print("clear - Clear the console...")

    def show_all(self):
        print(f"Developer Mode Information:\nCrypto: {self.crypto:.2f}, Money: ${self.money:.2f}, Miners: {self.miners}, Miner Level: {self.miner_level}, Upgrade Cost: ${self.miner_upgrade_cost}")
        self.dev_mode_commands()

    def add_money(self, command):
        try:
            amount = float(command.split()[1])
            self.money += amount
            print(f"Added ${amount:.2f} to your money. New balance: ${self.money:.2f}")
        except ValueError:
            print("Invalid amount.")

    def add_crypto(self, command):
        try:
            amount = float(command.split()[1])
            self.crypto += amount
            print(f"Added {amount:.2f} crypto. New balance: {self.crypto:.2f}")
        except ValueError:
            print("Invalid amount.")

    def set_miners(self, command):
        try:
            amount = int(command.split()[1])
            self.miners = amount
            print(f"Set number of miners to {self.miners}.")
        except ValueError:
            print("Invalid number.")

    def set_miner_level(self, command):
        try:
            level = int(command.split()[1])
            self.miner_level = level
            min_mine, max_mine = self.miner_efficiency(self.miner_level)
            print(f"Set miner level to {self.miner_level}. Now mines between {min_mine} and {max_mine} crypto per minute per miner.")
        except ValueError:
            print("Invalid level.")

    def upgrade_miner(self):
        self.miner_level += 1
        self.money -= self.miner_upgrade_cost
        self.miner_upgrade_cost = int(self.miner_upgrade_cost * 1.5)
        min_mine, max_mine = self.miner_efficiency(self.miner_level)
        print(f"Upgraded miners to level {self.miner_level}. Now mines between {min_mine} and {max_mine} crypto per minute per miner.")
        print(f"Remaining money: ${self.money:.2f}. Next upgrade cost: ${self.miner_upgrade_cost}")

    def run(self):
        auto_mine_thread = threading.Thread(target=self.auto_mine, daemon=True)
        auto_mine_thread.start()

        while self.running:
            command = input("CMD> ").strip().lower()
            self.process_command(command)

if __name__ == "__main__":
    game = CryptoGame()
    game.run()
