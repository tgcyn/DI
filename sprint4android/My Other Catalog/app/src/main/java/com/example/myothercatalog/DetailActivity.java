package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

//esta actividad mostrara el titulo, la imagen y la descripcion del libro q cliquemos
public class DetailActivity extends AppCompatActivity {
    private TextView titulo;
    private ImageView imagen;
    private TextView descripcion;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        //obtener el intent de la clase
        Intent intent = getIntent();

        //creo una variable para recuperar cada uno de los datos enviados en ViewHolder
        String tit = getIntent().getStringExtra("titulo");
        String img = getIntent().getStringExtra("imagen");
        String des = getIntent().getStringExtra("description");

        //creo un nuevo metodo para q muestre los datos recuperados
        visualizarDatos(tit, img, des);
    }

    private void visualizarDatos(String tit, String img, String des) {
        titulo = findViewById(R.id.TW_Titulo);
        titulo.setText(tit);

        imagen = findViewById(R.id.Im_Titulo);
        Glide.with(this).load(img).into(imagen); //esto hace q se visualice la imagen

        descripcion = findViewById(R.id.TW_Descripcion);
        descripcion.setText(des);
    }
}