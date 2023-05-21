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
peers="a0f726a3dffb45d9cbde0913701bd757fcd7e434@157.90.2.254:36656,344d9c933f936f79f3d62eff5cd0b82775a79dac@162.19.239.230:26656,84af58201840781a0a62449d1dcdb0ad0cf5bdb3@91.223.3.144:26356,e4e93ce4b050c9d821e15b69477f5da706121343@65.109.93.152:31656,f3e70d3de1974208af04dac6fabd657ab4abf0ff@65.108.75.107:24656,09d9127972ded9e22f9f11833ed7fcfa149cf1fa@65.109.92.240:19126,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13756,2cdaa56d0778b20be8430069eefeab2138190355@78.46.106.75:37656,3c6d856a429224201d78c7f28026874d10a27f57@5.75.227.78:26656,fabb22d283df1698de657c2bf4084892362136d6@38.242.237.107:26676"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
