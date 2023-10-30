package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    private Context context;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        context = this;

        //EJERCICIO 2
        Button b1 = findViewById(R.id.primerButton); //creo una instancia button para ligarlo con el escrito en el xml

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) { //este metodo indica q, cuando se pulse el boto, haga la accion especificada
                Intent intent = new Intent(context, DetailActivity.class); //intent permite abrir la segunda actividad, tengo q dar dos parámetros: 1)la clase en la q estoy (context) 2)la clase q quiero iniciar (DetailActivity) espsdificada como clase (.class)
                startActivity(intent); //esto hace q empiece la actividad
            }
        });

    }
}