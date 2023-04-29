# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" alt=""><figcaption></figcaption></figure>

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

**live-peers** (28)
```bash
peers="06f673591d9302c2beab5130b77bbb0a6a69364d@116.202.227.117:50656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,97a388be825fc69fca40a8a3de75aa5794602abb@95.217.225.212:36656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,ed367ee00b2155c743be6f5b635de6e7ea5acc64@149.202.73.104:11356,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,a1a6edee9e7928c97d8f99805757c09a1248b942@194.195.87.28:34656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,17a5fad48064ee3da42f435925f7bbe055e6348d@65.108.233.102:37656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,1aa11a85ea0ac04d720ddf15b605fd000e262ac1@128.140.60.175:26656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,4ffdad68a6c6302168e0951766ffa1921c9b19a4@199.175.98.136:26656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,b314955720069e8c98acf1cf1e896b68a3e306f9@65.108.4.161:27656,2223f5bf494729b9e9fdf6693d116d34e9d29755@141.94.193.28:55756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
