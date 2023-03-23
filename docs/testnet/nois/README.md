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

**live-peers** (20)
```bash
peers="0845590c7b9ac5d3a9813d1e06dfdf76c49f5876@142.132.209.236:17356,0e88031f79f4aa005b966324decba5ade4787efb@162.55.223.152:26656,72cd4222818d25da5206092c3efc2c0dd0ec34fe@161.97.96.91:36656,3bebfaee488ce50a1a3c9d5c4c5daea1991da9a3@89.58.18.47:26959,fa51a34d907a7680e0622f676d24709ebc148e00@162.19.31.150:55726,3df817ffc01f7cbf360620f8fe3ba2a3de925d58@212.23.222.109:26456,40250630b11b62814410129ed5dc29221e141a2f@65.108.72.233:26156,f9179f009a0351a51cde673929f751cc0ca4dfc3@95.217.2.24:26656,e2c0a70930d3df0ea6b274ae73b4982b96492de4@65.108.233.109:17356,91f2416b553b819b904c7e2b7823af3a7885e4d2@65.108.158.51:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:51656,a87dc8b4e827a05fe5c46aea54999120c8252587@162.19.237.81:26656,7b94b17a9eb14e1e263c20e4f395a4b0f0bc1978@192.95.30.128:26656,6d584f7501018441efa3815ad4d50619075708f0@65.108.195.235:13656,f2315b5ce33cb2d2e0e4098dbf593b23710e995f@38.242.221.64:30656,d82bc6935b0bcc2f44c29775176b422bbe737c9e@85.114.142.151:26656,2fd09098fe74fb45d1fe1d5aca190df6c9eeefd1@65.108.75.32:26656,9904ddc3186ea1e85390b8753da0e84948c1cf63@168.119.120.76:26656,55b593887e758eeb7c1c6e3f8ffd8b30eabd0069@65.108.82.62:26656,c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
