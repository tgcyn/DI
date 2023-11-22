package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

//esta actividad mostrara el titulo, la imagen y la descripcion del libro q cliquemos
public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
    }
}