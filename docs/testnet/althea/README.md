# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:15290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:15256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:15259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (32)
```bash
peers="3f9a20277d68b7fe52efbe84dad231af472d0190@162.55.235.69:29656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,bdf94092f6dc380f6526f7b8b46b63192e95a033@173.212.222.167:29656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,bc8e4351b85c930ab31ff178e5f15cf0b8536f31@66.94.101.5:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,d26fddea7ceb8cb5a52223702a23757cb09fad37@207.180.199.115:31656,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,3b4e352fe0164b220bae482225641b01aa6475d9@141.95.97.28:11356,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
