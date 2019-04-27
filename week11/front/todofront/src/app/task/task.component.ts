import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ITask, ITaskList} from '../shared/models/models';

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {

public taskLists:ITaskList[]=[];
public task:ITask[]=[]

 constructor(private provider:ProviderService) {
 }


 ngOnInit() {
   this.provider.getTaskLists().then(res => {
     this.taskLists = res
   });

 }

}
