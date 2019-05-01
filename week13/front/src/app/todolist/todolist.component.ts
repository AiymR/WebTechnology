import { Component, OnInit } from '@angular/core';
import { ProviderService } from "../shared/services/provider.service";
import { ITaskList, ITask } from "../shared/models/models";

@Component({
  selector: 'app-todolist',
  templateUrl: './todolist.component.html',
  styleUrls: ['./todolist.component.css']
})
export class TodolistComponent implements OnInit {
public taskLists :ITaskList[]=[];
public name: any = "";
public updateMode = false;
public current_list: ITaskList;
public logged = false;
public login: any ="" ;
public password: any = "";
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if(token){
      this.logged=true;
}
    if(this.logged){
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });

}
}
createTaskList() {
          if (this.name !== "") {
            this.provider.createTaskList(this.name).then(res => {
              this.taskLists.push(res);
              this.name = "";
              this.provider.getTaskLists().then(r => {
                this.taskLists = r;
              });
            });
          }
        }

updateTaskList(taskList: ITaskList) {
    this.updateMode=true;
    this.current_list = taskList;
    this.provider.updateTaskList(taskList).then(res => {});
  }

  deleteTaskList(c: ITaskList) {
      this.provider.deleteTaskList(c.id).then(res => {
        this.provider.getTaskLists().then(r => {
          this.taskLists = r;
        });
      });
    }

  auth(){
    if(this.login!=='' && this.password!==''){
      this.provider.auth(this.login,this.password).then(res=>{
        localStorage.setItem('token',res.token);
        this.logged=true;
        this.provider.getTaskLists().then(r => {
          this.taskLists = r;
        });
      })
    }
  }
  logout(){
    this.provider.logout().then(res => {
      localStorage.clear();
      this.logged=false;
    });
  }

}
