# Services

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
peers="16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,6655b2be870706c16d417ab15dd82a60fda0a0bd@78.46.61.117:01656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,1f1d115b9a70aa72f321bae376b1c6e44bab4668@24.17.14.167:46656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,87b67a8758306c61f8bb7504a0881cc837373633@140.82.38.208:26656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
