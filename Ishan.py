import datetime
import time
import winsound
import threading
import pandas as pd

class MedicationReminder:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, reminder_time, medicine_name):
        self.reminders.append((reminder_time, medicine_name))

    def set_medication_reminder(self, reminder_time, medicine_name):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == reminder_time:
                print(f"Reminder: It's time to take your {medicine_name}!")
                print()
                self.play_reminder_sound()
                self.display_next_medicine_in_queue()
            time.sleep(60)  # Check every minute

    def play_reminder_sound(self):

        winsound.Beep(440, 2000)  # Frequency: 440Hz, Duration: 1000ms

    def set_medication_reminders(self):
        threads = []
        for reminder in self.reminders:
            reminder_time, medicine_name = reminder
            thread = threading.Thread(target=self.set_medication_reminder, args=(reminder_time, medicine_name))
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    def display_medication_schedule(self):
        schedule_data = {'Time': [], 'Medication': []}
        for reminder in self.reminders:
            reminder_time, medicine_name = reminder
            schedule_data['Time'].append(reminder_time)
            schedule_data['Medication'].append(medicine_name)

        schedule_df = pd.DataFrame(schedule_data)
        print(schedule_df)
        print()

    def display_next_medicine_in_queue(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        next_medicine = None
        next_medicine_time = None

        for reminder in self.reminders:
            reminder_time, medicine_name = reminder
            if reminder_time > current_time:
                if next_medicine_time is None or reminder_time < next_medicine_time:
                    next_medicine = medicine_name
                    next_medicine_time = reminder_time

        if next_medicine:
            print(f"The next medicine in the queue is {next_medicine} and should be taken at {next_medicine_time}.")
            print()
        else:
            print("No upcoming medicine reminders in the queue.")

    def display_next_medicine(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        next_medicine = None
        next_medicine_time = None

        for reminder in self.reminders:
            reminder_time, medicine_name = reminder
            if reminder_time >= current_time:
                next_medicine = medicine_name
                next_medicine_time = reminder_time
                break

        if next_medicine:
            print(f"The next medicine is {next_medicine} and should be taken at {next_medicine_time}.")
            print()
        else:
            print("No upcoming medicine reminders.")
            print()

    def take_medicine(self, medicine_name):
        current_time = datetime.datetime.now().strftime("%H:%M")
        for i, reminder in enumerate(self.reminders):
            reminder_time, name = reminder
            if name == medicine_name:
                if reminder_time == current_time:
                    print(f"You have taken {medicine_name}.")
                    self.reminders.pop(i)
                    if len(self.reminders) > 0:
                        next_medicine = self.reminders[i][1]
                        next_medicine_time = self.reminders[i][0]
                        print(f"The next medicine is {next_medicine} and should be taken at {next_medicine_time}.")
                        self.display_next_medicine_in_queue()
                    break
                else:
                    print(f"It's not time to take {medicine_name} yet.")
                    break
        else:
            print(f"No reminder found for {medicine_name}.")

    def start_medication_reminder_system(self):
        self.display_medication_schedule()
        self.display_next_medicine()
        self.set_medication_reminders()

current_time = datetime.datetime.now().strftime("%H:%M")
dum1 =int(current_time[4])+1
dum2 =int(current_time[4])+2
c1=current_time[:4]+ str(dum1)
c2=current_time[:4]+ str(dum2)


reminder_system = MedicationReminder()
reminder_system.add_reminder(c1, "Aspirin")
reminder_system.add_reminder(c2, "Ibuprofen")
reminder_system.add_reminder("16:00", "Calcium supplement")

reminder_thread = threading.Thread(target=reminder_system.start_medication_reminder_system)
reminder_thread.start()


while True:
    time.sleep(1)
