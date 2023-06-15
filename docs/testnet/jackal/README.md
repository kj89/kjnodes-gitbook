# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v2.0.1 | **Wasm**: ON

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
peers="a0f726a3dffb45d9cbde0913701bd757fcd7e434@157.90.2.254:36656,34bb04a3e226493e5d142c74bf78d2ed2803ee9d@213.133.100.172:27464,27238e2f804bf28a14c186a2e0f0ceaae0d2588f@176.9.98.24:30566,344d9c933f936f79f3d62eff5cd0b82775a79dac@162.19.239.230:26656,11b91d243d43e761c96cfbf49f2f2bd06cce2df8@65.109.23.114:17556,fd5b3021fe67406e63c1a3e3e89cb243bc0791c9@65.109.32.174:32656,3c6d856a429224201d78c7f28026874d10a27f57@5.75.227.78:26656,2cdaa56d0778b20be8430069eefeab2138190355@78.46.106.75:37656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
