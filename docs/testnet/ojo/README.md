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
peers="d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,7831b3b3d625757c749d17569c6730f6589d35fe@65.109.48.181:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,622e5b7bc26be4edc4a9112ed0c5c8b00aa72721@185.246.84.196:26656,0a54815282d06cd10ce30b5ba3f9721c6ca1b600@135.181.33.42:50656,4640b6c775c05b6146a708a3b5ec2241c1688588@161.97.147.255:50656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,030c769628e3e56928f8fd143ce9bd9ce53dba34@31.220.85.212:46656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
