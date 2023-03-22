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

**live-peers** (16)
```bash
peers="cd4d60a32771919dc1c6242202b7b03959c2d34f@81.0.248.57:17356,c53187e34d66494bb5ec89445008fad4a8517c83@65.109.5.235:21656,0e88031f79f4aa005b966324decba5ade4787efb@162.55.223.152:26656,3bebfaee488ce50a1a3c9d5c4c5daea1991da9a3@89.58.18.47:26959,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:51656,f4ed6f6bdf086cbaab9bed20e4dfc1daf326e4fc@89.117.50.54:26656,7b94b17a9eb14e1e263c20e4f395a4b0f0bc1978@192.95.30.128:26656,3df817ffc01f7cbf360620f8fe3ba2a3de925d58@212.23.222.109:26456,f9179f009a0351a51cde673929f751cc0ca4dfc3@95.217.2.24:26656,7e5f4bb8c1c0045874aea8bd0a29eb50ad4b2aad@185.196.21.43:26656,ab4ec36768ff11f2ac806f3b29640cd245e4ad8c@195.154.94.166:23940,c971d1a5a18a8d781f5dccf13df9391cb4ffc282@65.108.225.158:17356,d82bc6935b0bcc2f44c29775176b422bbe737c9e@85.114.142.151:26656,e2c0a70930d3df0ea6b274ae73b4982b96492de4@65.108.233.109:17356,658fdd2411003be669e4317d365b3efde2bf941a@31.220.87.206:21656,4f4cbbb89deacb0a1f395050567e96bb70f4a1ff@142.132.152.46:41656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
