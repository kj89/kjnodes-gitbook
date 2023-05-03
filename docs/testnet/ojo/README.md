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

**live-peers** (9)
```bash
peers="c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,20d9bb13b09c054c30f1b48fbd276aa255af5a34@65.108.238.147:37656,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15056,b16d876c443850cd358596790411b835d3f1735b@95.214.53.46:35656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,fe8c46222c3a013115797176623597aafc16e33a@173.212.203.238:46656,5af3d50dcc231884f3d3da3e3caecb0deef1dc5b@142.132.134.112:25356,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
