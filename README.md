# Assignment-Kratin

The code demonstrates a medication reminder system using Python. It allows users to set reminders for taking their medications at specific times. The code utilizes threading to run the reminder system continuously without manual intervention.

The `MedicationReminder` class represents the medication reminder system. It has the following key functionalities:

1. Adding Reminders: The `add_reminder` method allows users to add medication reminders by specifying the reminder time and the name of the medicine.

2. Setting Medication Reminders: The `set_medication_reminders` method starts separate threads for each reminder using the `set_medication_reminder` method. Each thread continuously checks the current time and triggers the reminder when the reminder time matches the current time.

3. Displaying Medication Schedule: The `display_medication_schedule` method shows a table with the scheduled medication times and corresponding medicine names.

4. Displaying Next Medicine: The `display_next_medicine` method displays the next medicine that needs to be taken based on the current time.

5. Taking Medicine: The `take_medicine` method allows users to indicate that they have taken a particular medicine. It removes the corresponding reminder from the list and displays the next medicine to be taken, if applicable.

6. Reminder Sound: The `play_reminder_sound` method plays a sound (system beep) when a medication reminder is triggered.

7. Displaying Next Medicine in Queue: The `display_next_medicine_in_queue` method displays the next medicine in the queue based on their respective reminder times.

To use the medication reminder system, you can create an instance of the `MedicationReminder` class and add reminders using the `add_reminder` method. Then, start the reminder system by creating a thread and calling the `start_medication_reminder_system` method. The system will continuously monitor the reminders and display the medication schedule, the next medicine to be taken, and the next medicine in the queue.

The code runs dynamically and automatically displays reminders and updates information as the time progresses, without requiring manual intervention.

After running the code keep the screen still for atleast 5 min , it will give 2 beep sounds and the corresponding reminder for next medicine.
