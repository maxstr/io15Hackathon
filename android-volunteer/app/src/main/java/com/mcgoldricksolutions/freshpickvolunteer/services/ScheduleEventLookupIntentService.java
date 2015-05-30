package com.mcgoldricksolutions.freshpickvolunteer.services;

import android.app.IntentService;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.content.Context;
import android.os.PowerManager;
import android.support.v4.app.NotificationCompat;
import android.util.Log;
import android.widget.RemoteViews;

import com.commonsware.cwac.wakeful.WakefulIntentService;
import com.mcgoldricksolutions.freshpickvolunteer.FullscreenActivity;
import com.mcgoldricksolutions.freshpickvolunteer.MainActivity;
import com.mcgoldricksolutions.freshpickvolunteer.R;

/**
 * An {@link IntentService} subclass for handling asynchronous task requests in
 * a service on a separate handler thread.
 * <p/>
 * TODO: Customize class - update intent actions, extra parameters and static
 * helper methods.
 */
public class ScheduleEventLookupIntentService extends WakefulIntentService {

    private static String PACKAGE_NAME = "com.mcgoldricksolutions.freshpickvolunteer";

    RemoteViews mContentView = new RemoteViews(PACKAGE_NAME, R.layout.custom_notification);

    private PendingIntent mPendingIntent;
    private Intent mNotificationIntent;

    public ScheduleEventLookupIntentService() {
        super("ScheduleEventLookupIntentService");
    }

    @Override
    protected void doWakefulWork(Intent intent) {

        String title = "Awake";
        String content = "We are here";

        mContentView.setImageViewResource(R.id.image, R.drawable.ic_launcher);
        mContentView.setTextViewText(R.id.title, "Pickers needed, are you available?");
//        mContentView.setTextViewText(R.id.yes, "Yes");
//        mContentView.setTextViewText(R.id.no, "No");

        mNotificationIntent = new Intent(getApplicationContext(), MainActivity.class);
        mPendingIntent = PendingIntent.getActivity(getApplicationContext(), 0, mNotificationIntent, PendingIntent.FLAG_UPDATE_CURRENT);


        PowerManager pm = (PowerManager) getApplicationContext()
                .getSystemService(Context.POWER_SERVICE);
        PowerManager.WakeLock wakeLock = pm.newWakeLock(
                PowerManager.PARTIAL_WAKE_LOCK, "");
        wakeLock.acquire();

        Notification.Builder notificationBuilder = new Notification.Builder(
                getApplicationContext())
                .setSmallIcon(R.drawable.ic_stat_notify)
                .setContentTitle(title)
                .setDefaults(Notification.DEFAULT_ALL)
                .setContent(mContentView)
                .setAutoCancel(true)
                .setContentIntent(mPendingIntent)
                .setContentText(content);


        NotificationManager notificationManager = (NotificationManager) getApplicationContext()
                .getSystemService(Context.NOTIFICATION_SERVICE);
        notificationManager.notify(0, notificationBuilder.build());

        wakeLock.release();

        //Log.d(getClass().getSimpleName(), "I ran!");
    }

}
