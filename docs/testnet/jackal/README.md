# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v1.2.0-beta.4 | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)




## Chain explorer
[https://explorer.kjnodes.com/jackal-testnet](https://explorer.kjnodes.com/jackal-testnet)

## Public endpoints

* api: [https://jackal-testnet.api.kjnodes.com](https://jackal-testnet.api.kjnodes.com)
* rpc: [https://jackal-testnet.rpc.kjnodes.com](https://jackal-testnet.rpc.kjnodes.com)
* grpc: [https://jackal-testnet.grpc.kjnodes.com](https://jackal-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@jackal-testnet.rpc.kjnodes.com:37656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@jackal-testnet.rpc.kjnodes.com:37659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal-testnet/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (14)
```bash
peers="2ededbdbd98580e22ae8c3676e37b6e1fc1d987b@142.132.248.253:23656,3e3dabb71f85f8f142b31495f9b012424f90c3f4@57.128.80.37:26656,0e3058446ee9b1ad449b5d3a60d5c4f92dd3785c@65.109.30.12:56656,0394449cab5a29f24dd4f37683d3b7622f27c0fc@65.108.206.118:61156,11b91d243d43e761c96cfbf49f2f2bd06cce2df8@65.109.23.114:17556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:37656,372111fd8c3c11a57cd34db58b2bdd8d2b6e5005@172.104.19.93:26656,6c6c7f370febd64447770da8aec0b9d359d61565@65.109.70.23:17556,451622fd913f6119a67f67e65f3ab82c3fbea529@78.107.253.133:32656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,3c6d856a429224201d78c7f28026874d10a27f57@5.75.227.78:26656,b549c1092e37db22576e31f19cbec4b1b3b36503@116.202.227.117:37656,fa10dc1a1dc81ee2741e7f88327cb13d2ab56f54@65.109.23.182:19126,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26906"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
