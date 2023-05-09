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
peers="d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,ec003ade1f7c57d822a1be56c838e668b755bee5@94.190.90.38:33656,b33500a3aaeb7fa116bdbddbe9c91c3158f38f8d@128.199.18.172:26656,7d6706d7ee674e2b2c38d3eb47d85ec6e376c377@49.12.123.87:56656,affee2f485ca15c68c302ad98e8de41fcd0e71ba@162.19.238.49:26656,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,8fbfa810cb666ddef1c9f4405e933ef49138f35a@65.108.199.120:54656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
