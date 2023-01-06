from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String())
    release_date = db.Column(db.Date())
    total_inventory = db.Column(db.Integer())
    #customer = db.relationship("Customer", back_populates="videos")

    def to_dict(self):
        video_as_dict = {}
        video_as_dict["id"] = self.id
        video_as_dict["title"] = self.title
        video_as_dict["release_date"] = self.release_date
        video_as_dict["total_inventory"] = self.total_inventory
        
        return video_as_dict

    @classmethod
    def from_dict(cls, video_data):
        new_video = Video(
            title=video_data["title"],
            release_date=video_data["release_date"],
            total_inventory=video_data["total_inventory"],
           
                        )
        return new_video
