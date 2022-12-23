# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)


## Public endpoints

* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (10)
```
peers="1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,143c212edac4e29e00218214205f1011d7376b02@135.181.38.11:26656,c2c7344a10a39040592a8aa156ef9da17700d9a2@45.84.0.252:26656,959a47a00ab4c95a149cc20936a5206842d5c0e5@95.217.186.152:21656,3c4f8aa4bf226c331b32d93f51f089e47e753279@194.163.155.84:36656,ac7bcba48b364f46bea2b614c997a025d676986e@78.25.145.168:46656,d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,dd81f3ff364a09080364da0d3ade47b3cb10d324@167.235.142.77:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,d53006a0db9a2eac79f853526719716cece550ad@144.76.92.112:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
