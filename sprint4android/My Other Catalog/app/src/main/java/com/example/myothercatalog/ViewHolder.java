package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

//contiene el diseño de un elemento de la lista y como se organizan los datos (Data) dentro de ella
public class ViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;

    public ViewHolder(@NonNull View itemView) {
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.texto_celda);
        imageView = (ImageView) itemView.findViewById(R.id.imagen_celda);
    }

    //este metodo sirve para cargar los datos y la imagen
    public void showData(Data data, Activity activity) {
        textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into(imageView);
    }
}


