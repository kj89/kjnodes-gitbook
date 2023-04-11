# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" width="150" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.2.3 | **Wasm**: OFF

[Website](https://twitter.com/elys_network) | [Discord](https://discord.gg/R9Gr6Vh7vC) | [Twitter](https://twitter.com/elys_network)



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

**live-peers** (9)
```bash
peers="15263a87a09f90ba71d35cbddf17ff5178e9b133@65.21.225.10:40656,9e456e22da0930be2761123b7036e386a3247647@57.128.110.141:26656,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,0cbf883987ff0c8e72f6c75331b2af01c8074946@51.159.223.41:26656,3f75a8743a5b9242cfbb57652defe540a4c1a5d4@137.184.154.151:26656,701a382e03978c54f1176145460125516b6a4672@3.144.113.232:26656,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,f3480371baafae419bfef68a64ace00dd8944bd6@65.109.92.241:10126"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
