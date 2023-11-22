package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

//crea tantas celdas como yo le indique con las especificaciones del viewHolder
public class Adapter extends RecyclerView.Adapter<ViewHolder> {
    private List<Data> allTheData;
    private Activity activity;

    //metodo constructor q reciba toda la informacion q devemos mostrar
    public Adapter(List<Data> allTheData, Activity activity) {
        this.allTheData = allTheData;
        this.activity = activity;
    }

    @NonNull
    @Override
    //este metodo es el q crea la celda
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.view_holder, parent, false);
        return new ViewHolder(view); //con esto invocamos ViewHolder, q es el q determina la forma q tiene cada elemento
    }

    @Override
    //"determina" la informacion q debe mostrar la celda
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Data dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    @Override
    //da el numero de elementos q se van a mostrar el la lista
    public int getItemCount() {
        return allTheData.size(); //al usar .size() le estoy indicando q se muestren todos los elementos de la lista
    }
}
