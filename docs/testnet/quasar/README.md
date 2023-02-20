# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: qsr-questnet-04 | **Latest Version Tag**: v0.0.2-alpha-11 | **Wasm**: ON

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)




## Chain explorer
[https://explorer.kjnodes.com/quasar-testnet](https://explorer.kjnodes.com/quasar-testnet)

## Public endpoints

* api: [https://quasar-testnet.api.kjnodes.com](https://quasar-testnet.api.kjnodes.com)
* rpc: [https://quasar-testnet.rpc.kjnodes.com](https://quasar-testnet.rpc.kjnodes.com)
* grpc: [https://quasar-testnet.grpc.kjnodes.com](https://quasar-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quasar-testnet.rpc.kjnodes.com:48656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quasar-testnet.rpc.kjnodes.com:48659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar-testnet/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (32)
```bash
peers="04a6cd559f0d490202b4926905a6b65ed20cf7b7@65.21.232.160:53656,08e7f2b6dcb630cb53b907018d7e9916922ecb21@137.184.160.32:2686,136589c157a21094c976f67bcb76bc6327c58b93@65.108.97.58:2686,fa76aa585cbe520508edb02ec627667128bf928c@65.109.117.23:48656,8964b8b854d21c72821cbe704daf463aea1f5327@167.172.73.246:53656,fdc1babb7ad4d97a911d32b0545220c8ceca57a8@128.199.8.206:53656,949b3f703062a56106ae64db50c828c20bf460f3@95.216.220.183:48656,57e32fc17c16f0bb16110cbfc043738d3b4ad5c6@138.201.91.105:48656,c49a1bb49ac30163fc879efaf08b76c2e46d0c16@210.75.253.161:26656,b2bf4609b1b736ff2e28521dbf0977f768d58a32@61.220.197.176:48656,79da889f34e249c017092d22e5da27ce615eebe3@188.34.178.190:48656,9ad3b058f1dd84a87102ada4471343dea4f40ed6@188.34.178.184:48656,f8f5cf44fc2e574fede651f51c87f153df49b876@95.217.212.233:48656,3955ca59db742538e6198209b464f29a2f3485ea@95.217.211.135:48656,6df8c9f71a8543f83368cfd30bef5332c3ac28c7@146.190.35.147:53656,47ced1ad4be0c7953085f69ff5a351187cd0aabe@161.97.92.139:53656,b35f3493df8c3be232fe75ef7f4d0cb9d0f59668@65.109.70.23:18256,99876203eb2f455eaf99fa80f4cf95c94c0bd600@5.161.86.216:48656,45242cf33bdebea72f1ef173a0df69bec7640a1e@173.249.50.126:48656,84762cde38156b2c2b03f7065ef1305fe5061210@195.201.237.188:48656,b8c9bde24b0f012a83bd0c5bb6b1a93d4d652fcf@95.216.159.0:48656,c7e5e8976f24099dd2fa82de172388144ea0ec7c@85.10.199.157:48656,1c5dd597b2edd6f16d659c5273de1fbc3c3d0e3f@116.202.227.117:48656,796a79aee66959005dfe99bf41bc3f8a20186f12@65.109.9.255:48656,7c6bc7f805be6e84c6cf7030896ed3b0f4aaa635@95.217.217.253:48656,c77145d485d62fb8ee5fa987dcf66726f8741bb3@46.0.203.78:23636,91e0c99770db7b8cf7e6e3f8685f0eb5c65cdc04@161.97.160.209:26656,b1197bd0946b3d2d462fcc7548a79e87101d2389@65.108.141.109:38656,966acc999443bae0857604a9fce426b5e09a7409@65.108.105.48:18256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:48656,23998555a8cdde840f04c0a0728435e7e72f5bbd@65.109.4.229:29656,2c1e9f7f0ca923172052139b20b75b877a4fbcf9@43.155.109.94:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
