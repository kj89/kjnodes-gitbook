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

**live-peers** (29)
```bash
peers="cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,6cbb393c7b4b061a3b63d8061e67ce8fcf53f8d6@95.214.55.109:2626,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,33d16e5cfd73bd8b600da03a0ac93f2a38691315@77.54.1.75:1202,f8a62360e6084b6a9ba3f731a1fb708ef3c9c5cf@143.198.136.136:28656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,83a0043b2a2bfff38c3725c70f4c0305c760dfef@213.239.207.175:47656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,9dc1f555bd37d6840237f32a2cd4d79ba1c80cb5@65.108.227.112:31656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,7d6706d7ee674e2b2c38d3eb47d85ec6e376c377@49.12.123.87:56656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,06f673591d9302c2beab5130b77bbb0a6a69364d@116.202.227.117:50656,4e309b79b9147a0243f6e0cbc824f86e10bd09de@65.109.234.254:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,1879aa588b4d6431bf40543f3a44129dcf60a043@144.91.77.68:50656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
