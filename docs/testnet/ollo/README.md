# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (19)
```
peers="60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,a99fc4e81770ca32d574cac2e8680dccc9b55f74@18.144.61.148:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,377008a2fb0f98dfd15a4a38b9a751a5a3b56446@135.181.104.247:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
