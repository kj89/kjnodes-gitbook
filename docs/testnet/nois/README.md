# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" width="150" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-testnet-004 | **Latest Version Tag**: v0.6.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisNetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nois-testnet](https://explorer.kjnodes.com/nois-testnet)

## Public endpoints

* api: [https://nois-testnet.api.kjnodes.com](https://nois-testnet.api.kjnodes.com)
* rpc: [https://nois-testnet.rpc.kjnodes.com](https://nois-testnet.rpc.kjnodes.com)
* grpc: nois-testnet.grpc.kjnodes.com:51090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nois-testnet.rpc.kjnodes.com:51656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nois-testnet.rpc.kjnodes.com:51659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois-testnet/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:51656,7e5f4bb8c1c0045874aea8bd0a29eb50ad4b2aad@185.196.21.43:26656,3bebfaee488ce50a1a3c9d5c4c5daea1991da9a3@89.58.18.47:26959,c89ccec23799848505e1ecf7d3a36cdbe9046273@65.109.90.162:17656,3df817ffc01f7cbf360620f8fe3ba2a3de925d58@212.23.222.109:26456,72cd4222818d25da5206092c3efc2c0dd0ec34fe@161.97.96.91:36656,e2c0a70930d3df0ea6b274ae73b4982b96492de4@65.108.233.109:17356,a87dc8b4e827a05fe5c46aea54999120c8252587@162.19.237.81:26656,40250630b11b62814410129ed5dc29221e141a2f@65.108.72.233:26156,f4ed6f6bdf086cbaab9bed20e4dfc1daf326e4fc@89.117.50.54:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
