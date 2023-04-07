# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.7 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/hypersign-testnet](https://explorer.kjnodes.com/hypersign-testnet)

## Public endpoints

* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)
* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* grpc: hypersign-testnet.grpc.kjnodes.com:31090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (26)
```bash
peers="55b3cf307182091e60b774712733231a8cc7f448@89.163.132.156:31656,28fa150b5a843c9bdf2889f31f4ff8ac75c17be9@185.196.20.153:26656,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,3ca31590349f5a1480163e4a802cdc6b6ee25328@65.108.131.99:21339,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,934324c3b4318d8438954d19a82673a3d218951b@142.132.209.236:10956,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,4e08d5b0cb43c8d5ffc42987a5166bab2a04a93b@65.109.92.240:21066,eaf27acc810a3d6728dde972ebad26810cce0ae6@65.108.229.233:26656,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.158:26926,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,62c3f3e5214495593ad204f3c6cd879f3f4ed6a9@5.9.79.121:26656,23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,1acc83715399737cff74767e00807d1d402eb1e2@144.91.65.175:26656,001668e85c4f7b6ff796b3b593e485cd67223f0c@85.190.254.14:31656,de1f980cc59bdb2457202768d4b4d964d783789e@167.235.21.165:36656,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,c127e8b0608e62709b690037a6b0da635c6f5447@89.58.45.204:56656,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,a3f3d6dba11bfe080693938666064b2324fbaccf@88.99.164.158:11056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
