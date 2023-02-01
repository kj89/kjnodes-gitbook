# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v1.2.0-beta.1 | **Wasm**: ON

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

**live-peers** (15)
```bash
peers="2ededbdbd98580e22ae8c3676e37b6e1fc1d987b@142.132.248.253:23656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,11b91d243d43e761c96cfbf49f2f2bd06cce2df8@65.109.23.114:17556,09d9127972ded9e22f9f11833ed7fcfa149cf1fa@65.109.92.240:19126,f3e70d3de1974208af04dac6fabd657ab4abf0ff@65.108.75.107:24656,6c6c7f370febd64447770da8aec0b9d359d61565@65.109.70.23:17556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:37656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26906,372111fd8c3c11a57cd34db58b2bdd8d2b6e5005@172.104.19.93:26656,1f11577400a5caadedc01261e0f4902983445fb1@46.4.53.94:26656,fa10dc1a1dc81ee2741e7f88327cb13d2ab56f54@65.109.23.182:19126,0394449cab5a29f24dd4f37683d3b7622f27c0fc@65.108.206.118:61156,fd5b3021fe67406e63c1a3e3e89cb243bc0791c9@65.109.32.174:32656,3e3dabb71f85f8f142b31495f9b012424f90c3f4@57.128.80.37:26656,b549c1092e37db22576e31f19cbec4b1b3b36503@116.202.227.117:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
