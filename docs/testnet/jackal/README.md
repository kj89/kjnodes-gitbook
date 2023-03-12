# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v1.2.0-beta.7 | **Wasm**: ON

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

**live-peers** (28)
```bash
peers="b549c1092e37db22576e31f19cbec4b1b3b36503@116.202.227.117:37656,2ededbdbd98580e22ae8c3676e37b6e1fc1d987b@142.132.248.253:23656,1b191fb9ef837dec648136097f94925a15dd85ab@213.170.135.20:26516,fd5b3021fe67406e63c1a3e3e89cb243bc0791c9@65.109.32.174:32656,075c59c5917e4e41fcb3e28dba80292a457f79ea@65.108.57.170:26656,11b91d243d43e761c96cfbf49f2f2bd06cce2df8@65.109.23.114:17556,80420ad774e622bda8e1dfa9b80da11eee7eed1f@144.126.140.252:29656,ff5171d91cb033670238998dc84bdf69468bb053@51.89.232.234:27686,2cdaa56d0778b20be8430069eefeab2138190355@78.46.106.75:37656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:37656,e4e93ce4b050c9d821e15b69477f5da706121343@65.109.93.152:31656,0394449cab5a29f24dd4f37683d3b7622f27c0fc@65.108.206.118:61156,09d9127972ded9e22f9f11833ed7fcfa149cf1fa@65.109.92.240:19126,9a2c091798681f89b11f8eea370bf9c6284437c5@167.86.115.183:26656,3c6d856a429224201d78c7f28026874d10a27f57@5.75.227.78:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26906,451622fd913f6119a67f67e65f3ab82c3fbea529@78.107.253.133:32656,84af58201840781a0a62449d1dcdb0ad0cf5bdb3@91.223.3.144:26356,344d9c933f936f79f3d62eff5cd0b82775a79dac@162.19.239.230:26656,0e3058446ee9b1ad449b5d3a60d5c4f92dd3785c@65.109.30.12:56656,f3e70d3de1974208af04dac6fabd657ab4abf0ff@65.108.75.107:24656,d3677c7a3f9ef42d5ba213ae84c4c5749f4ee787@44.204.38.21:26656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,a0f726a3dffb45d9cbde0913701bd757fcd7e434@157.90.2.254:36656,34bb04a3e226493e5d142c74bf78d2ed2803ee9d@213.133.100.172:27464,4ea723e652f11433734ae2aa6f364ef0510d6636@16.163.74.176:26626,6c6c7f370febd64447770da8aec0b9d359d61565@65.109.70.23:17556,fa10dc1a1dc81ee2741e7f88327cb13d2ab56f54@65.109.23.182:19126"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
