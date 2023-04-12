# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" width="150" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.2.3 | **Wasm**: OFF

[Website](https://elys.network) | [Discord](https://discord.gg/R9Gr6Vh7vC) | [Twitter](https://twitter.com/elys_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/elys-testnet](https://explorer.kjnodes.com/elys-testnet)

## Public endpoints

* api: [https://elys-testnet.api.kjnodes.com](https://elys-testnet.api.kjnodes.com)
* rpc: [https://elys-testnet.rpc.kjnodes.com](https://elys-testnet.rpc.kjnodes.com)
* grpc: elys-testnet.grpc.kjnodes.com:53090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@elys-testnet.rpc.kjnodes.com:53656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@elys-testnet.rpc.kjnodes.com:53659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/elys-testnet/addrbook.json > $HOME/.elys/config/addrbook.json
```

**live-peers** (25)
```bash
peers="ee401fbe1afe6546f78c8e0f5ee0ff8922a45b06@192.3.164.17:26656,f6480d5563172e7de0b97b666c4d503d7c4daae8@94.130.225.23:26656,0cbf883987ff0c8e72f6c75331b2af01c8074946@51.159.223.41:26656,d9f2e28e398d42fe7ca8ed322ee168b3e867bc95@65.108.199.222:34656,3f75a8743a5b9242cfbb57652defe540a4c1a5d4@137.184.154.151:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,df8a39358aaa5d188f59ead77540bc96cf374f82@65.108.9.50:56656,d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,3183a894566bbc5a4d55df6bf3636d2a9a942550@65.109.38.111:22056,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,4404a413b2f2a6ac20aa0424960972528bbcc9ff@31.220.84.183:27656,86987eeff225699e67a6543de3622b8a986cce28@91.183.62.162:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,42d3a20613e443087ae5aec1f1e56c0a12cf8455@135.181.60.184:46656,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,eb07af5b4c6c0a208cdd8ca0187fe5da2e2602c2@64.226.103.162:26656,85f34862d3195daaeb6853369bd0439ed1804e8a@159.89.27.173:21956,1af9a47eae993ea84752fff373ec2c7eb27d5918@145.224.88.118:26656,734a87b41a015faf59a7d6266deea190421476c2@95.217.160.243:26656,af23cecc6b675b5785905199579de84ba36b0a10@65.109.175.192:53656,2357548a7ba90a7d4a99b047d9b449f376d70e1c@167.71.213.61:21956,54114ce29b4625d75760851e71921d27bba0032a@157.245.201.247:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
