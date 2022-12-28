# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v1.2.0-alpha.7 | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)


## Public endpoints

* rpc: [https://jackal-testnet.rpc.kjnodes.com](https://jackal-testnet.rpc.kjnodes.com)
* api: [https://jackal-testnet.api.kjnodes.com](https://jackal-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@jackal-testnet.rpc.kjnodes.com:37656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@jackal-testnet.rpc.kjnodes.com:37659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/jackal-testnet/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (25)
```
peers="3c6d856a429224201d78c7f28026874d10a27f57@5.75.227.78:26656,f3e70d3de1974208af04dac6fabd657ab4abf0ff@65.108.75.107:24656,0e3058446ee9b1ad449b5d3a60d5c4f92dd3785c@65.109.30.12:56656,a76cb9a09652ad3f62987966dda2199a0ee1bf64@65.109.90.33:17556,84af58201840781a0a62449d1dcdb0ad0cf5bdb3@91.223.3.144:26356,451622fd913f6119a67f67e65f3ab82c3fbea529@78.107.253.133:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:37656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26906,c28ae12dc190b2abfc578f8ed2fea90fa5ff3b1d@65.108.134.208:26656,9a2c091798681f89b11f8eea370bf9c6284437c5@167.86.115.183:26656,372111fd8c3c11a57cd34db58b2bdd8d2b6e5005@172.104.19.93:26656,09d9127972ded9e22f9f11833ed7fcfa149cf1fa@65.109.92.240:19126,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,2633208f609ac5fc77fac203dd23326ba0fc9902@185.208.207.94:26656,6c7100291f35132ac1b58ff7c6d05b4ce75512b7@65.108.70.119:36156,0394449cab5a29f24dd4f37683d3b7622f27c0fc@65.108.206.118:61156,b26f63f307ca8e80033cbc618f7577e5be7f0c1a@95.217.118.96:27363,4ea723e652f11433734ae2aa6f364ef0510d6636@16.163.74.176:26626,2ededbdbd98580e22ae8c3676e37b6e1fc1d987b@142.132.248.253:23656,1b191fb9ef837dec648136097f94925a15dd85ab@213.170.135.20:26516,80420ad774e622bda8e1dfa9b80da11eee7eed1f@144.126.140.252:29656,b549c1092e37db22576e31f19cbec4b1b3b36503@116.202.227.117:37656,9b2bbd5121265ebbf9003341e8a2e0abdbc24b67@46.228.199.8:26656,a0f726a3dffb45d9cbde0913701bd757fcd7e434@157.90.2.254:36656,6c6c7f370febd64447770da8aec0b9d359d61565@65.109.70.23:17556"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
