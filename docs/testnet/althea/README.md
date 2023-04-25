# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (36)
```bash
peers="ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,a7b4e2ab0e3334bd2986c09cd5dafbc938ef23bf@65.108.78.101:52656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,6655b2be870706c16d417ab15dd82a60fda0a0bd@78.46.61.117:01656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,29dbc6241210d67e3460e2994e803bb2695dd71a@27.79.250.190:26656,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656,4ff3241de49fa01129b3fe38b3aeefc699f07cc7@58.187.173.207:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,26e70e13195b0d04cda0fca1f7b16b8746a620ed@65.109.28.226:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
