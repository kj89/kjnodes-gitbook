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
* grpc: althea-testnet.grpc.kjnodes.com:52090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:52656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:52659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (27)
```bash
peers="cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,79d18c52d35ddd204f61e9be8aa3c7b35d75cab7@65.108.139.20:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,6655b2be870706c16d417ab15dd82a60fda0a0bd@78.46.61.117:01656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,733e9d5f995c2866df9f2e1254551940f060a70c@51.159.159.112:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:12456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
