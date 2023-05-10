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
peers="c0ee71c74858b339787320596b805ed631c48ebb@213.133.100.172:27433,855fc154f9054ce4055719e09ce6f7f1d0ecd9fb@85.10.198.171:36656,6e5726d52ed6c854cc0625b32981dd93c01b54d7@135.181.183.62:17656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,8fbfa810cb666ddef1c9f4405e933ef49138f35a@65.108.199.120:54656,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,b33500a3aaeb7fa116bdbddbe9c91c3158f38f8d@128.199.18.172:26656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,0a54815282d06cd10ce30b5ba3f9721c6ca1b600@135.181.33.42:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
