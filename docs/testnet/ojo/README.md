# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:50090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:50656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:50659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (30)
```bash
peers="8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,c0ee71c74858b339787320596b805ed631c48ebb@213.133.100.172:27433,d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,e052b7c899bae41f6d89f70f81de50e28b72a7bf@38.242.237.100:26656,69ffa3745aa4ff20756fe66153619a52f348d1ef@139.59.142.164:50656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,17a5fad48064ee3da42f435925f7bbe055e6348d@65.108.233.102:37656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,0e5e110fc015fd3cdd4b465fbedf6218ffc5e9ee@65.108.78.101:50656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
