class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def is_added(objects, object):
        if object in objects:
            return True
        return False

    def add_customer(self, customer):
        if not self.is_added(self.customers, customer):
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not self.is_added(self.trainers, trainer):
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not self.is_added(self.equipment, equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not self.is_added(self.plans, plan):
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not self.is_added(self.subscriptions, subscription):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ""
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                result += f"{subscription.__repr__()}\n"
                for customer in self.customers:
                    if customer.id == subscription.customer_id:
                        result += f"{customer.__repr__()}\n"
                for trainer in self.trainers:
                    if trainer.id == subscription.trainer_id:
                        result += f"{trainer.__repr__()}\n"

                for exercise in self.plans:
                    if exercise.id == subscription.exercise_id:
                        for eq in self.equipment:
                            if eq.id == exercise.equipment_id:
                                result += f"{eq.__repr__()}\n"

                        result += f"{exercise.__repr__()}"
            return result
