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

**live-peers** (30)
```bash
peers="001668e85c4f7b6ff796b3b593e485cd67223f0c@85.190.254.14:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,934324c3b4318d8438954d19a82673a3d218951b@142.132.209.236:10956,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,eaf27acc810a3d6728dde972ebad26810cce0ae6@65.108.229.233:26656,4e08d5b0cb43c8d5ffc42987a5166bab2a04a93b@65.109.92.240:21066,28fa150b5a843c9bdf2889f31f4ff8ac75c17be9@185.196.20.153:26656,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,62c3f3e5214495593ad204f3c6cd879f3f4ed6a9@5.9.79.121:26656,a275d8018f683f279bf5167a72d294bfacafa839@178.63.102.172:41656,d72875380d7b0b68f071623996bd5a86b7491287@116.202.227.117:31656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.158:26926,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,54f5df8d6516ead7099191776d9ee2048e0ec947@95.214.53.46:26656,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,0c6758a3f4554bbc67da73993bbb697764c5c534@38.242.142.227:26656,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,1acc83715399737cff74767e00807d1d402eb1e2@144.91.65.175:26656,5e4fc955b23ab00f6a07cb6d56e89aafac0c85ff@167.86.85.122:26656,e9bf8e034cfb29658d252f81633ab91e9f28df26@65.109.89.5:27656,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,de1f980cc59bdb2457202768d4b4d964d783789e@167.235.21.165:36656,63db727618b237d4a27656aa456be2812154bf29@65.109.170.47:26656,a3f3d6dba11bfe080693938666064b2324fbaccf@88.99.164.158:11056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
