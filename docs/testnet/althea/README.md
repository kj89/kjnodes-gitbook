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

**live-peers** (32)
```bash
peers="ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,eb69783b7e38059a58abaf342eb64f704de37636@23.88.66.239:31656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,4a8c845bdffc8bae0ed0e91a476bc57720adec15@65.108.206.74:26656,d4d84619ea7b89dbad3a637ba7e475ba9bcd3606@173.8.192.30:26656,766377592cbaae65d8e6df5120bd8b4fdfc8a372@98.63.20.2:26656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
