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
peers="02f12e71d5150b49c39123e4e979999b1a08e99d@5.9.79.121:62656,21f35146e8905d6786b69486b1d27b680fb3c548@65.109.89.5:40656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,18300f0a5973798c3900fe51ff255bb6bca982f9@65.109.65.248:36656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,17a5fad48064ee3da42f435925f7bbe055e6348d@65.108.233.102:37656,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
