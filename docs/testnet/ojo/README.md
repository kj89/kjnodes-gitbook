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

**live-peers** (11)
```bash
peers="91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,b33500a3aaeb7fa116bdbddbe9c91c3158f38f8d@128.199.18.172:26656,3e2d9912684b16ad98d25b46535c24c496749277@185.144.99.81:26656,ed367ee00b2155c743be6f5b635de6e7ea5acc64@149.202.73.104:11356,da9e028814ff30ec24e94bec6887f4686f692b86@173.212.222.167:30656,02f12e71d5150b49c39123e4e979999b1a08e99d@5.9.79.121:62656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
