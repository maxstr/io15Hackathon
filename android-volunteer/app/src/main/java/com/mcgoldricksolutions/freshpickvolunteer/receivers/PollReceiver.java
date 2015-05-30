package com.mcgoldricksolutions.freshpickvolunteer.receivers;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.SystemClock;
import com.mcgoldricksolutions.freshpickvolunteer.services.ScheduleEventLookupIntentService;

import com.commonsware.cwac.wakeful.WakefulIntentService;

public class PollReceiver extends BroadcastReceiver {
    private static final int PERIOD= 60 * 1000; // 1 minutes
    private static final int INITIAL_DELAY=5000; // 5 seconds

    @Override
    public void onReceive(Context ctxt, Intent i) {
        if (i.getAction() == null) {
            WakefulIntentService.sendWakefulWork(ctxt, ScheduleEventLookupIntentService.class);
        }
        else {
            scheduleAlarms(ctxt);
        }
    }

    public static void scheduleAlarms(Context ctxt) {
        AlarmManager mgr=
                (AlarmManager)ctxt.getSystemService(Context.ALARM_SERVICE);
        Intent i=new Intent(ctxt, PollReceiver.class);
        PendingIntent pi=PendingIntent.getBroadcast(ctxt, 0, i, 0);

        mgr.setRepeating(AlarmManager.ELAPSED_REALTIME_WAKEUP,
                SystemClock.elapsedRealtime() + INITIAL_DELAY,
                PERIOD, pi);

    }
}
