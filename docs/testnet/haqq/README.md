# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: haqq-testnet.grpc.kjnodes.com:35090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,88b8b733d8b96e9a518c1a8bea4dbc5bf896026e@5.161.156.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,442d3bacb350437b8d9f0f1431e0519b81094100@135.181.62.222:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,230d299006a432b0f44534ca8a19c8c876c0ccb3@85.10.193.246:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,331ca63236ba05842d561e22c0bcc8582efa60a1@209.126.80.192:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,d7ac44bf8f8d760c3df1a8695145021f35feb985@34.88.220.124:26656,8238ddf162ce8a144610e671c63226b0207a1f73@38.242.148.96:36656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.18:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,8865bf7e0575d3033b54d41854ed117ee40983bd@3.125.7.6:26656,bb9c3d1c6fb845602f9f595802765fc86a0f3b10@154.26.137.198:26656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,6de69146d5ebbc0b8cd9ecdf4b33edb57bf9b559@185.187.170.133:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,5b2ee53c742ce5d392b93c8f193f489a4f13f685@5.189.186.222:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
