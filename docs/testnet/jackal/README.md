# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v1.2.2-alpha.1 | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/jackal-testnet](https://explorer.kjnodes.com/jackal-testnet)

## Public endpoints

* api: [https://jackal-testnet.api.kjnodes.com](https://jackal-testnet.api.kjnodes.com)
* rpc: [https://jackal-testnet.rpc.kjnodes.com](https://jackal-testnet.rpc.kjnodes.com)
* grpc: jackal-testnet.grpc.kjnodes.com:37090

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

**live-peers** (22)
```bash
peers="3aaeda343f226f9f2f00eeda53a20db438449c8c@89.58.45.204:46656,09d9127972ded9e22f9f11833ed7fcfa149cf1fa@65.109.92.240:19126,84af58201840781a0a62449d1dcdb0ad0cf5bdb3@91.223.3.144:26356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:37656,cf3921d374ad226e4b2248626c285302cba5e55e@141.95.33.39:26656,11b91d243d43e761c96cfbf49f2f2bd06cce2df8@65.109.23.114:17556,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26906,2cdaa56d0778b20be8430069eefeab2138190355@78.46.106.75:37656,9a2c091798681f89b11f8eea370bf9c6284437c5@167.86.115.183:26656,dc84774683298e57a848b59b7c0d1a70477b4fc1@213.239.207.175:48656,344d9c933f936f79f3d62eff5cd0b82775a79dac@162.19.239.230:26656,0394449cab5a29f24dd4f37683d3b7622f27c0fc@65.108.206.118:61156,1b191fb9ef837dec648136097f94925a15dd85ab@213.170.135.20:26516,27238e2f804bf28a14c186a2e0f0ceaae0d2588f@176.9.98.24:30566,fd5b3021fe67406e63c1a3e3e89cb243bc0791c9@65.109.32.174:32656,ec78732a7d5bdc1e27e8d7ac1bffe3881c9fb271@65.108.226.183:17556,a0f726a3dffb45d9cbde0913701bd757fcd7e434@157.90.2.254:36656,4ea723e652f11433734ae2aa6f364ef0510d6636@16.163.74.176:26626,451622fd913f6119a67f67e65f3ab82c3fbea529@78.107.253.133:32656,d3677c7a3f9ef42d5ba213ae84c4c5749f4ee787@44.204.38.21:26656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,8a11570dbaa0f4d98ca2ef0ad117e9c1154d81b9@65.108.230.113:19126"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
