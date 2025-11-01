import random
import string

# -----------------------------
# User and Wallet Classes
# -----------------------------
class Wallet:
    def __init__(self):
        self.points = 0

    def add_points(self, amount):
        self.points += amount
        print(f"✅ {amount} points added! Current balance: {self.points}")

    def redeem_points(self, amount):
        if amount > self.points:
            print("❌ Not enough points to redeem.")
        else:
            self.points -= amount
            print(f"🎁 {amount} points redeemed successfully! Remaining balance: {self.points}")

class User:
    def __init__(self, name):
        self.name = name
        self.referral_code = self.generate_referral_code()
        self.referred_by = None
        self.wallet = Wallet()

    def generate_referral_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# -----------------------------
# Referral System
# -----------------------------
class ReferralSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, name, referral_code=None):
        user = User(name)
        self.users[user.referral_code] = user

        if referral_code and referral_code in self.users:
            referrer = self.users[referral_code]
            user.referred_by = referrer.name
            print(f"👥 {user.name} was referred by {referrer.name}.")
        else:
            print(f"👤 {user.name} registered without a referral.")

        print(f"🔑 {user.name}'s referral code: {user.referral_code}")
        return user

    def make_purchase(self, user, amount):
        print(f"\n💰 {user.name} made a purchase worth ₹{amount}.")

        # Base reward points (e.g., 10% of purchase value)
        earned_points = int(amount * 0.1)
        user.wallet.add_points(earned_points)

        # Reward referrer if exists
        if user.referred_by:
            referrer = next(u for u in self.users.values() if u.name == user.referred_by)
            referrer.wallet.add_points(earned_points)
            print(f"🎉 Referral reward: {referrer.name} and {user.name} both earned {earned_points} points!")

    def show_wallet(self, user):
        print(f"\n💼 {user.name}'s Wallet Balance: {user.wallet.points} points")

# -----------------------------
# Simulation
# -----------------------------
if __name__ == "__main__":
    system = ReferralSystem()

    # Step 1: Register main user
    alice = system.register_user("Alice")

    # Step 2: Alice shares her referral code
    print(f"\n🔗 Alice shares referral code: {alice.referral_code}")

    # Step 3: Bob registers using Alice's referral code
    bob = system.register_user("Bob", referral_code=alice.referral_code)

    # Step 4: Bob makes a purchase
    system.make_purchase(bob, 500)

    # Step 5: Check both wallets
    system.show_wallet(alice)
    system.show_wallet(bob)

    # Step 6: Bob redeems points
    bob.wallet.redeem_points(20)

    # Step 7: Final wallet balances
    system.show_wallet(alice)
    system.show_wallet(bob)
