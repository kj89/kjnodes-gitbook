# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:15056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:15059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (10)
```bash
peers="0621bb73d18724cae4eb411e6b96765f95a3345e@178.63.8.245:61356,a1a6edee9e7928c97d8f99805757c09a1248b942@194.195.87.28:34656,13589ee5424836988c1ced68e023679c99163a6c@91.142.78.203:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,7d59fd87e149226d58d28846a17711ec8b89888c@65.109.122.105:60956,17a5fad48064ee3da42f435925f7bbe055e6348d@65.108.233.102:37656,ed367ee00b2155c743be6f5b635de6e7ea5acc64@149.202.73.104:11356,6e0b45d32722df1a612d723e289e59ede65a9dd1@65.109.61.113:24214,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,e73e29131fca25c0aa3da698f76ff708a361f16a@65.109.99.212:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
