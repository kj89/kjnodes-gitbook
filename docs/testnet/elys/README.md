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

**live-peers** (16)
```bash
peers="9e456e22da0930be2761123b7036e386a3247647@57.128.110.141:26656,0cbf883987ff0c8e72f6c75331b2af01c8074946@51.159.223.41:26656,42d3a20613e443087ae5aec1f1e56c0a12cf8455@135.181.60.184:46656,5e6b0be59463073b41499365b8c25a24ad5a07a5@141.98.112.138:61656,8d9845f7ef934ade824981b9145a26f00192b575@45.79.24.206:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,3183a894566bbc5a4d55df6bf3636d2a9a942550@65.109.38.111:22056,00c65e06302fb35a1064d9aa4e528aaf98925aa8@65.108.105.48:22056,f3480371baafae419bfef68a64ace00dd8944bd6@65.109.92.241:10126,ae22b82b1dc34fa0b1a64854168692310f562136@198.27.74.140:26656,d907ce9285951a2a063789df2f6bd4cc86b33d53@142.132.155.178:16656,db03e6915cad62b2646ae72566ed19074a7707b6@95.217.144.107:22056,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,df8a39358aaa5d188f59ead77540bc96cf374f82@65.108.9.50:56656,d9f2e28e398d42fe7ca8ed322ee168b3e867bc95@65.108.199.222:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
