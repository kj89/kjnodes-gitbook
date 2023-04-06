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

**live-peers** (27)
```bash
peers="efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,2641ddcf28d8adf448edb573de1efba0b6971d9e@178.154.222.128:26656,91089c0911b59f59fe2ec79fdae017f9beefbbfd@65.108.101.158:26656,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,de1f980cc59bdb2457202768d4b4d964d783789e@167.235.21.165:36656,4e08d5b0cb43c8d5ffc42987a5166bab2a04a93b@65.109.92.240:21066,934324c3b4318d8438954d19a82673a3d218951b@142.132.209.236:10956,28fa150b5a843c9bdf2889f31f4ff8ac75c17be9@185.196.20.153:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,62c3f3e5214495593ad204f3c6cd879f3f4ed6a9@5.9.79.121:26656,d72875380d7b0b68f071623996bd5a86b7491287@116.202.227.117:31656,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,15d2f1bc2bfaa143388465ea115c59e5ce6e77dc@65.109.39.223:26656,cf94099349980f9593a3f0362c85fe7c6eda8b14@8.219.48.59:26656,55b3cf307182091e60b774712733231a8cc7f448@89.163.132.156:31656,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,eaf27acc810a3d6728dde972ebad26810cce0ae6@65.108.229.233:26656,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,3ca31590349f5a1480163e4a802cdc6b6ee25328@65.108.131.99:21339,a3f3d6dba11bfe080693938666064b2324fbaccf@88.99.164.158:11056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
