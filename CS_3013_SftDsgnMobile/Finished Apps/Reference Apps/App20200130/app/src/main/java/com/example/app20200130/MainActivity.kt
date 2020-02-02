package com.example.app20200130

import android.content.res.Resources
import android.graphics.Color
import android.graphics.Color.red
import android.os.Bundle
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.view.View.GONE
import android.view.View.VISIBLE
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import android.widget.ToggleButton
import kotlinx.android.synthetic.*

import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.content_main.*
import kotlinx.android.synthetic.main.content_main.view.*

class MainActivity : AppCompatActivity() {




    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)
        help_msg.visibility = GONE
        toggleButton.visibility = GONE
        toggleButton2.visibility = GONE
        ok_button.visibility = GONE

        toggleButton2.setOnCheckedChangeListener { buttonView, isChecked ->
            if (isChecked) {
                // The toggle is enabled/checked
                Toast.makeText(applicationContext,"Toggle on",Toast.LENGTH_SHORT).show()
                help_msg.visibility = VISIBLE
            } else {
                // The toggle is disabled
                Toast.makeText(applicationContext,"Toggle off",Toast.LENGTH_SHORT).show()
                help_msg.visibility = GONE
            }
        }

        // Set a click listener for root layout object
        toggleButton2.setOnClickListener{
            // Get the toggle button state programmatically
            if(toggleButton2.isChecked){
                // If toggle button is checked/on then
                // The toggle is enabled/checked
                Toast.makeText(applicationContext,"Toggle on",Toast.LENGTH_SHORT).show()
                help_msg.visibility = VISIBLE

            }else{
                // The toggle is unchecked
                Toast.makeText(applicationContext,"Toggle off",Toast.LENGTH_SHORT).show()
                help_msg.visibility = GONE

            }
        }

        toggleButton.setOnCheckedChangeListener { buttonView, isChecked ->
            if (isChecked) {
                // The toggle is enabled/checked
                Toast.makeText(applicationContext,"Changed Color",Toast.LENGTH_SHORT).show()
                help_msg.setBackgroundColor(Color.GREEN)
            } else {
                // The toggle is disabled
                Toast.makeText(applicationContext,"Changed Color",Toast.LENGTH_SHORT).show()
                help_msg.setBackgroundColor(android.R.drawable.btn_default)
            }
        }

        // Set a click listener for root layout object
        toggleButton.setOnClickListener{
            // Get the toggle button state programmatically
            if(toggleButton.isChecked){
                // If toggle button is checked/on then
                // The toggle is enabled/checked
                Toast.makeText(applicationContext,"Changed Color",Toast.LENGTH_SHORT).show()
            }else{
                // The toggle is unchecked
                Toast.makeText(applicationContext,"Changed Color",Toast.LENGTH_SHORT).show()
            }
        }


        // Set a click listener for the button widget
        ok_button.setOnClickListener{
            // Change the toggle button checked state on button click
            help_msg.visibility = GONE
            toggleButton.visibility = GONE
            toggleButton2.visibility = GONE
            ok_button.visibility = GONE
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        return when (item.itemId) {
            R.id.action_settings -> true
            R.id.action_help -> {

                help_msg.visibility = VISIBLE
                toggleButton.visibility = VISIBLE
                toggleButton2.visibility = VISIBLE
                ok_button.visibility = VISIBLE

                true

            }
            else -> super.onOptionsItemSelected(item)
        }
    }
}
