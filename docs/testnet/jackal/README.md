# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v2.0.0-rc.0 | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/jackal-testnet](https://explorer.kjnodes.com/jackal-testnet)

## Public endpoints

* api: [https://jackal-testnet.api.kjnodes.com](https://jackal-testnet.api.kjnodes.com)
* rpc: [https://jackal-testnet.rpc.kjnodes.com](https://jackal-testnet.rpc.kjnodes.com)
* grpc: jackal-testnet.grpc.kjnodes.com:13790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@jackal-testnet.rpc.kjnodes.com:13756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@jackal-testnet.rpc.kjnodes.com:13759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal-testnet/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```bash
peers="2cdaa56d0778b20be8430069eefeab2138190355@78.46.106.75:37656,344d9c933f936f79f3d62eff5cd0b82775a79dac@162.19.239.230:26656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,ff5171d91cb033670238998dc84bdf69468bb053@51.89.232.234:27686,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13756,0394449cab5a29f24dd4f37683d3b7622f27c0fc@65.108.206.118:61156,ec78732a7d5bdc1e27e8d7ac1bffe3881c9fb271@65.108.226.183:17556,dc84774683298e57a848b59b7c0d1a70477b4fc1@213.239.207.175:48656,fabb22d283df1698de657c2bf4084892362136d6@38.242.237.107:26676,b549c1092e37db22576e31f19cbec4b1b3b36503@116.202.227.117:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
