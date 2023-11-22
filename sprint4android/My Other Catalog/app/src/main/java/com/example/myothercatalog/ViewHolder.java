package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

//contiene el diseño de un elemento de la lista y como se organizan los datos (Data) dentro de ella
public class ViewHolder extends RecyclerView.ViewHolder {
    private TextView textView;
    private ImageView imageView;
    private Data titulo;

    public ViewHolder(@NonNull View itemView) {
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.texto_celda);
        imageView = (ImageView) itemView.findViewById(R.id.imagen_celda);

        //vamos a hacer q al clicar en la celda, se abra otra actividad
        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String nombre = titulo.getName();
                Context context = view.getContext();
                Toast.makeText(context, "Clicaste en el titulo: " + nombre, Toast.LENGTH_LONG).show();

                //iniciar una segunda actividad en la q mostrar info sobre el libro
                Intent intent = new Intent(context, DetailActivity.class);
                context.startActivity(intent);
            }
        });
    }

    //este metodo sirve para cargar los datos y la imagen
    public void showData(Data data, Activity activity) {
        this.textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into(this.imageView);
        this.titulo = data;
    }
}


