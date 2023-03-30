# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/gravitybridge](https://explorer.kjnodes.com/gravitybridge)

## Public endpoints

* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)
* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* grpc: gravitybridge.grpc.kjnodes.com:26090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (12)
```bash
peers="e5362a93c6e7f686d72c8d6d98be2c7bceeb5cc3@49.12.23.149:27010,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,6edddf41ca6bad0362c069afced6a9f0c67bd2a4@195.201.195.108:26656,162e8994c0738fb5895e77b888718ea51d4c40d3@167.86.106.22:26656,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,a8d25e5e9cae32ae50537e4c83673ad61d589517@65.108.107.100:26656,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656,e940c7788dfbf02030d0838fb3dc9cdb21cf5832@66.94.112.81:26656,70ff1535443969705182c9473cc66773fbc12c09@15.235.13.145:26656,ca4270ebed73b4d0982450aac16fe08860410fac@142.132.248.138:26626,9a8c4af7574a5d1fcd5e89f755348c7b6df3b4be@142.132.158.93:14256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
